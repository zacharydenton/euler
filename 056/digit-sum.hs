digits :: Integer -> [Integer]
digits 0 = []
digits n = r : digits q
    where (q, r) = quotRem n 10

main :: IO ()
main = print $ maximum [sum $ digits $ a^b | a <- [1..99], b <- [1..99]]
