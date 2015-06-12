package main

import "fmt"

func IsPalindrome(number int) bool {
	n := number
	reversed, digit := 0, 0
	for n > 0 {
		digit = n % 10
		reversed = reversed*10 + digit
		n /= 10
	}
	return number == reversed
}

func main() {
	product, max := 0, 0
	for a := 100; a < 1000; a++ {
		for b := a; b < 1000; b++ {
			product = a * b
			if product > max && IsPalindrome(product) {
				max = product
			}
		}
	}
	fmt.Println(max)
}
