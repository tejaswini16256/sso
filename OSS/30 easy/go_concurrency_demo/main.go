package main

import (
    "fmt"
    "math/rand"
    "sync"
    "time"
)

// simulateWork is a function that performs a "work" task, like processing data.
func simulateWork(id int, wg *sync.WaitGroup, results chan<- string) {
    defer wg.Done() // Signal completion of this goroutine
    time.Sleep(time.Duration(rand.Intn(1000)) * time.Millisecond) // Simulate variable processing time
    result := fmt.Sprintf("Worker %d finished work", id)
    results <- result // Send result to channel
}

func main() {
    rand.Seed(time.Now().UnixNano()) // Seed random number generator for varied sleep times
    var wg sync.WaitGroup            // WaitGroup to synchronize goroutines
    results := make(chan string, 5)  // Channel to collect results from workers

    // Start 5 goroutines
    for i := 1; i <= 5; i++ {
        wg.Add(1)
        go simulateWork(i, &wg, results)
    }

    // Close results channel when all goroutines are done
    go func() {
        wg.Wait() // Wait for all goroutines to finish
        close(results)
    }()

    // Print results as they arrive
    for result := range results {
        fmt.Println(result)
    }
}
