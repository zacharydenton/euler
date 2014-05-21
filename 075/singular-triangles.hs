import Data.Array

triples :: Int -> [Int]
triples limit = [a + b + c | u <- [1..l'], v <- [u+1,u+3..l'-u], gcd u v == 1,
                             let a = v^2 - u^2, let b = 2*u*v, let c = u^2 + v^2]
    where l' = round $ sqrt $ fromIntegral limit

perimeters :: Int -> Array Int Int
perimeters limit = accumArray (+) 0 (1, limit) $ map (\p -> (p, 1)) $ concat [takeWhile (<= limit) $ map (*p) [1..] | p <- triples limit]

main :: IO ()
main = print $ length $ filter (== 1) $ elems $ perimeters 1500000
