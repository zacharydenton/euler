import Data.List (sort)

pandigital :: String -> Bool
pandigital = (== "123456789") . sort

multiples :: Int -> [String]
multiples x = takeWhile ((== 9) . length) $ dropWhile ((< 9) . length) $ scanl (\acc n -> acc ++ show (x * n)) (show x) [2..]

main :: IO ()
main = putStrLn $ maximum $ filter pandigital $ concatMap multiples [1..10000]
