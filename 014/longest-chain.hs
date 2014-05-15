import Data.Word
import Data.Array

memoCollatz :: Array Word Word
memoCollatz = listArray (1, size) $ map collatz [1..size]
    where size = 1000000

collatz :: Word -> Word
collatz 1 = 1
collatz n | inRange (bounds memoCollatz) next = 1 + memoCollatz ! next
          | otherwise = 1 + collatz next
          where next = case n of
                           1 -> 1
                           n | even n -> n `div` 2
                             | otherwise -> 3 * n + 1

main = print $ snd $ maximum $ map (\n -> (collatz n, n)) [1..1000000]
