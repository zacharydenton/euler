import qualified Data.Set as Set

factorial :: Integer -> Integer
factorial n = product [1..n]

digits :: Integer -> [Integer]
digits 0 = []
digits n = r : digits q
    where (q, r) = quotRem n 10

next :: Integer -> Integer
next = sum . map factorial . digits

chain :: Integer -> Integer
chain = inner Set.empty where
    inner set x | Set.member x set = 0
                | otherwise = 1 + inner (Set.insert x set) (next x)

main :: IO ()
main = print $ length $ filter ((== 60) . chain) [1..1000000]
