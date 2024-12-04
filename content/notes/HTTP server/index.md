# HTTP servers

## Servers

Many different server stacks

- Go: Great performance whether the workload is I/O or CPU-bound
- Python / Django / Flask: ok in I/O task
  - Usually python apps handle single request at a time. WSGI saves the day by spinning up multiple python instances to handle diff req.
- Node.js / Express.js: Good in I/O but struggles in CPU-bound tasks.
  - Usually single threaded. Uses single cpu core. Handles many request via async event loops.

```
func main(){
	const port = "8080"
	mux := http.NewServeMux()
	server := &http.Server{
		Addr:    ":" + port,
		Handler: mux,
	}
	log.Printf("Serving on port: %s\n", port)
	server.ListenAndServe()
}
```

Very basics of hosting a server on localhost:8080

## Handlers vs Handlers func

```
	mux.Handle("/app/", http.StripPrefix("/app",
		http.FileServer(http.FileSystem(http.Dir(".")))))
	mux.HandleFunc("/healthz", handlerHealthz)
func handlerHealthz(w http.ResponseWriter, req *http.Request) {
	w.Header().Set("Content-Type", "text/plain; charset=utf-8")
	w.WriteHeader(200)
	w.Write([]byte("OK"))
}
```

A handler is an interface.

```
type Handler interface {
	ServeHTTP(ResponseWriter, *Request)
}
```

Handlers handles HTTP requests. Usually will be used to handle more complex task. HandlerFunc are used when you want to implement simpler handler.

```
type HandlerFunc func(ResponseWriter, *Request)
```

\*Request contains all info coming from client like method, path, headers, and body
ResponseWriter is mutable and we want to write to it. Think of it like changing a dict in Python.

```
def changeItem(dict):
	dict[item] = changed
```

So no copying required (less memory). Less chance of of bugs / mismatched data. Clarity

```
	apiCfg := apiConfig{}
	mux.Handle("/app/", http.StripPrefix("/app",
		apiCfg.middlewareMetricInc(
			http.FileServer(http.FileSystem(http.Dir("."))))))
	mux.HandleFunc("/healthz", handlerHealthz)
	mux.HandleFunc("/metrics", apiCfg.handlerMetric)
	mux.HandleFunc("/reset", apiCfg.handlerMetricReset)
func (cfg *apiConfig) handlerMetric(w http.ResponseWriter, req *http.Request) {
	result := fmt.Sprintf("Hits: %d\n", cfg.fileserverHits.Load())
	w.Header().Set("Content-Type", "text/plain; charset=utf-8")
	w.WriteHeader(200)
	w.Write([]byte(result))
}
func (cfg *apiConfig) handlerMetricReset(w http.ResponseWriter, req *http.Request) {
	cfg.fileserverHits.Store(0)
}
func (cfg *apiConfig) middlewareMetricInc(next http.Handler) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, req *http.Request) {
		cfg.fileserverHits.Add(1)
		next.ServeHTTP(w, req)
	})
}
type apiConfig struct {
	fileserverHits atomic.Int32
}
```

## Routing

```
	mux.HandleFunc("GET /healthz", handlerHealthz)
	mux.HandleFunc("GET /metrics", apiCfg.handlerMetric)
	mux.HandleFunc("POST /reset", apiCfg.handlerMetricReset)
```

Only allows /healthz, /metrics to be reached via GET request.

```
[Method ][HOST]/[PATH]
```

The above is a pattern. Will match pattern based on the longest string.
/assets/css/style.css will be handled by /assets/css/

## Storage

Memory vs Disk
When running a program, it will be in RAM but using it as storage isn't a good idea since it will be wiped on restart.

On disk it will be permanant. One of the ways to write to disk is a raw file, like json. Okay in some uses, but it will have issues with concurrency, scalability, and complexity. You won't be able to write write to the same file at same time. If you write a lot of code to deal with files, the higher chance of bugs. Read and writing large files will take a lot of disk space.

A database also writes to disk via files but comes with efficiency.

```zsh
brew install postgresql@15                 #install
brew services start postgresql@15          #starting server in background
psql postgres                              #connect to server
```

Connection string is all info needed to connect to a database.
`postgres://chichigami:@localhost:5432/chirpy`

Make an `.env` file with `DB_URL="YOUR_CONNECTION_STRING_HERE"`

We will need to import some drivers and libraries. Postgres driver needs to be imported even if we don't interact with it. godotenv package is used to read the `.env` file.

```
import (
	"github.com/chichigami/chirpy/internal/database"
	"github.com/joho/godotenv"
	_ "github.com/lib/pq"
)
func main(){
	godotenv.Load()
	dbURL := os.Getenv("DB_URL")
	db, err := sql.Open("postgres", dbURL)
	if err != nil {
		log.Fatalf("Error opening database: %s", err)
	}
	dbQueries := database.New(db)
}
```

## Architectures

### Monoliths and Decoupling

Coupling in this context would be the data and presentation logic of the data.
Front end: The presentation logic
In a web app, it would be HTML CSS JS

## Authentication

Types of authentication

- ID + Password

- 3rd party (google/github/discord/etc login)

- Magic links: sends link to user email and webserver will decode the unique token encoded in the email

- API keys: long secure string that uniquely identifies a user or system

### JSON Web Token (JWT)

Cryotgraphically signed JSON object about an authenticated user.

1. User submits user/pass.
2. Server sends JWT w/ user id and other info to client
3. On every authenticated req, server validates JWT
4. JWT expires and cycle repeats

JWT are stateless. So servers don't need to keep track of is logged in. Good for scalabiity.

### Refresh Token:

- Used to refresh JWT when they expire without the need to relog.
- Longer lifespan than JWT. Stored server side.
- If refresh token is valid and not expired, issue new JWT.

### Cookies

Cookie is a small piece of data that a server sends to a client. Example: an item in a shoping cart
Cookies are sent via http header `Set-Cookie` and are sent back to the server automatically via
`Cookie` header.

## Authorization

Veryifying what a user is allowed to do. Either if they make or delete their own content, or if they're an admin/mod.

## Webhooks

A webhook is an event that is sent to your server by 3rd party service. Example: Stripe to process payments
Stripe sends a webhook to server and we use that info. Example: Stripe sends webhook, we give membership
Webhooks often make multiple request. So the webhook handler needs to be idempotent (result is the same, can have side effects).
Process:

1. Person makes payment to Stripe
2. Stripe process payment
3. Stripe sends a HTTP POST request to http://api.example.com/stripe/webhook
4. We handle the request AND THEN we send back a 2XX code

**NOT THE SAME AS WEBSOCKETS**. Websockets is a persistent connection between client and server.

## RESTful API (CRUD API)

Conventional ways to make an API

```
GET      /videos            #all videos
GET      /videos/id         #/videos/2
POST     /videos            #create a video
PUT      /videos/id         #update a video
DELETE   /videos/id         #delete a video
```

Do not remove the plural convention. **DO NOT DO /video/id**
Usually DELETE /videos DOES NOT EXIST. Do not want to delete all videos from the platform

## Documentation

No API > Bad API
Because incorrect documentation is worse than not having anything.
