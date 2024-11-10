// main.go
package main

import (
	"fmt"
	"math/rand"
	"sync"
	"time"
)

// simulateWork performs a simulated work task with a random delay
func simulateWork(id int, wg *sync.WaitGroup, results chan<- string) {
	defer wg.Done()
	time.Sleep(time.Duration(rand.Intn(1000)) * time.Millisecond)
	result := fmt.Sprintf("Worker %d finished work", id)
	results <- result
}

func main() {
	rand.Seed(time.Now().UnixNano())
	var wg sync.WaitGroup
	results := make(chan string, 5)

	// Start 5 concurrent workers
	for i := 1; i <= 5; i++ {
		wg.Add(1)
		go simulateWork(i, &wg, results)
	}

	go func() {
		wg.Wait()
		close(results)
	}()

	for result := range results {
		fmt.Println(result)
	}
}
