parse :: String -> [[Integer]]
parse = map (map read . words) . lines

best :: [Integer] -> [Integer]
best row = map maximum choices where
    choices = zipWith (\a b -> a : [b]) row (tail row)

maxStep :: [Integer] -> [Integer] -> [Integer]
maxStep current next = zipWith (+) next (best current)

maxPath :: [[Integer]] -> Integer
maxPath [[x]] = x
maxPath (current:next:rest) = maxPath $ (maxStep current next) : rest

main :: IO ()
main = do
        str <- readFile "/home/zach/code/euler/018/triangle.txt"
        print $ maxPath $ reverse $ parse str
