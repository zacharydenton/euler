package main

import "fmt"

func main() {
	sumSquares, squareSum := 0, 0
	for i := 1; i <= 100; i++ {
		sumSquares += i * i
		squareSum += i
	}
	squareSum *= squareSum
	fmt.Println(squareSum - sumSquares)
}
