divisors ::  Integer -> [Integer]
divisors n = [x | x <- [1..(div n 2)], n `mod` x == 0]

d ::  Integer -> Integer
d = sum . divisors

isAmicable ::  Integer -> Bool
isAmicable n = n /= x && d x == n where x = d n

main ::  IO ()
main = print $ sum $ filter isAmicable [1..10000]
