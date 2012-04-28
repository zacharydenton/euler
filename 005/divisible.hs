isDivisibleTo ::  Integer -> Integer -> Bool
isDivisibleTo x n = all (\i -> n `mod` i == 0) (reverse [1..x])

divisibleTo ::  Integer -> Integer
divisibleTo 1 = 1
divisibleTo x = let step = divisibleTo (x-1)
                in  head $ filter (isDivisibleTo x) [step,2*step..]

main ::  IO ()
main = print $ divisibleTo 20
