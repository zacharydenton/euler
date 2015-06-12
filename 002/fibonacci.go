package main

import "fmt"

func main() {
	sum := 0
	for a, b := 1, 2; b <= 4e6; a, b = b, a+b {
		if b%2 == 0 {
			sum += b
		}
	}
	fmt.Println(sum)
}
