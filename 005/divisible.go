package main

import "fmt"

func GCD(a, b int) int {
	for b != 0 {
		a, b = b, a%b
	}
	return a
}

func main() {
	lcm := 1
	for i := 2; i <= 20; i++ {
		lcm *= i / GCD(i, lcm)
	}
	fmt.Println(lcm)
}
