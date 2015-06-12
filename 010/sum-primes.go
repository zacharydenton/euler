package main

import "fmt"
import "math"

func PrimeSieve(n int64) []int64 {
	result := make([]int64, 0, n/int64(math.Log(float64(n))))
	sieve := make([]bool, n+1)
	sn := int64(math.Sqrt(float64(n)))
	var i, j int64
	for i = 2; i <= sn; i++ {
		if !sieve[i] {
			for j = i * i; j <= n; j += i {
				sieve[j] = true
			}
		}
	}
	for i = 2; i <= n; i++ {
		if !sieve[i] {
			result = append(result, i)
		}
	}
	return result
}

func main() {
	primes := PrimeSieve(2000000)
	var sum int64 = 0
	for _, p := range primes {
		sum += p
	}
	fmt.Println(sum)
}
