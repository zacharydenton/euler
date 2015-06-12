package main

import "fmt"

func iSqrt(n int64) int64 {
	var r1, r int64 = n, n + 1
	for r1 < r {
		r, r1 = r1, (r1+n/r1)>>1
	}
	return r
}

func PrimeSieve(n int64) []int64 {
	result := make([]int64, 0, n)
	sieve := make([]bool, n+1)
	sn := iSqrt(n)
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
	primes := PrimeSieve(1000000)
	fmt.Println(primes[10000])
}
