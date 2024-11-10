// main_test.go
package main

import (
	"sync"
	"testing"
)

// TestSimulateWork verifies that simulateWork sends the correct result format to the channel.
func TestSimulateWork(t *testing.T) {
	var wg sync.WaitGroup
	results := make(chan string, 1) // Buffered channel to collect the result

	wg.Add(1)
	go simulateWork(1, &wg, results)

	// Wait for simulateWork to complete
	go func() {
		wg.Wait()
		close(results)
	}()

	// Check the result
	result := <-results
	expected := "Worker 1 finished work"
	if result != expected {
		t.Errorf("Expected %s, but got %s", expected, result)
	}
}
