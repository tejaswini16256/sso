package main

import (
        "fmt"
        "sync"
)

func worker(id int, jobs <-chan int, results chan<- int, wg *sync.WaitGroup) {
        defer wg.Done()
        for j := range jobs {
                fmt.Printf("Worker %d processing job %d\n", id, j)
                results <- j * 2
        }
}

func main() {
        var wg sync.WaitGroup
        jobs := make(chan int, 100)
        results := make(chan int, 100)

        for w := 0; w < 3; w++ {
                wg.Add(1)
                go worker(w, jobs, results, &wg)
        }

        for j := 1; j <= 9; j++ {
                jobs <- j
        }
        close(jobs)
        wg.Wait()
        close(results)

        for r := range results {
                fmt.Println("Result:", r)
        }
}