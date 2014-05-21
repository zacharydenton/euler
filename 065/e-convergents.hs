convergents :: [Integer]
convergents = 2 : concat [[1, 2*k, 1] | k <- [1..]]

rationalize :: [Integer] -> (Integer, Integer)
rationalize = foldr (\x (n, d) -> (x*n + d, n)) (1, 0)

digits :: Integer -> [Integer]
digits 0 = []
digits n = r : digits q
    where (q, r) = quotRem n 10

main :: IO ()
main = print $ sum $ digits $ fst $ rationalize $ take 100 convergents
