package main

import "fmt"
import "math"
import "math/big"

func eratosthenes(max int) []int {
	nums := make([]int, max)

	p := 2 // first prime, 2
	for {
		i := p - 1
		// mark multiples not prime
		for i += p; i < max; i += p {
			nums[i] = -1
		}
		// find first unmarked number greater than p
		for i = p; i < max; i++ {
			if nums[i] != -1 {
				p = i + 1
				break
			}
		}
		// no unmarked numbers greater than p found; finished
		if i == max {
			break
		}
	}
	// filter out all marked numbers
	primes := make([]int, max)
	j := 0
	for i := range nums {
		if nums[i] == 0 {
			primes[j] = i + 1
			j++
		}
	}
	return primes[:j]
}

func main() {
	n := new(big.Int)
	n.SetString("600851475143", 10)
	m := new(big.Int)
	max := int(math.Sqrt(600851475143))
	primes := eratosthenes(max)
	// find the largest prime factor of n
	for i := len(primes) - 1; i >= 0; i-- {
		p := big.NewInt(int64(primes[i]))
		m.Mod(n, p)
		if m.Int64() == 0 {
			fmt.Println(p)
			break
		}
	}
}
