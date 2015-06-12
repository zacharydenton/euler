package main

import "fmt"

func main() {
	var a, b, c, lb int
	max := 1000
	for a = 1; a < max; a++ {
		lb = max - a
		for b = a; b < lb; b++ {
			c = max - (a + b)
			if a*a+b*b == c*c {
				fmt.Println(a * b * c)
				return
			}
		}
	}
}
