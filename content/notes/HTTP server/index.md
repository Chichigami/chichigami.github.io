# HTTP servers

## Goals

- Understand what web servers are
- Build a production style HTTP server without framework
- Use JSON, headers, status codes to communicate with client via RESTful API
- Use typesafe SQL to store and retrieve data from Postgres db
- Implement secure auth system w/ crypto libs
- Build and understand webhooks
- Document REST API w/ MD

## Servers

Many different server stacks

- Go: Great performance whether the workload is I/O or CPU-bound
- Python / Django / Flask: ok in I/O task
  - Usually python apps handle single request at a time. WSGI saves the day by spinning up multiple python instances to handle diff req.
- Node.js / Express.js: Good in I/O but struggles in CPU-bound tasks.
  - Usually single threaded. Uses single cpu core. Handles many request via async event loops.

```go
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
	mux.Handle("/app/", http.StripPrefix("/app", http.FileServer(http.FileSystem(http.Dir(".")))))
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

	mux.Handle("/app/", http.StripPrefix("/app", apiCfg.middlewareMetricInc(http.FileServer(http.FileSystem(http.Dir("."))))))
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

## Architectures

### Monoliths and Decoupling

Coupling in this context would be the data and presentation logic of the data.
Front end: The presentation logic
In a web app, it would be HTML CSS JS

## Authentication vs Authorization

Authentication: Verify a user via some method like password, api key, 2fa, etc
Authorization: ALLOWS a verified user to do an action. Like discord mod vs kitten

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

DO NOT remove the plural convention. **DO NOT DO /video/id**
Usually DELETE /videos DOES NOT EXIST. Do not want to delete all videos from the platform
