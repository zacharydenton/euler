factorial :: Int -> Int
factorial n = product [1..n]

digits :: Int -> [Int]
digits 0 = []
digits n = r : digits q
    where (q, r) = quotRem n 10

curious :: Int -> Bool
curious n = n == sum (map factorial (digits n))

main :: IO ()
main = print $ sum $ filter curious [10..50000]
