#!/usr/bin/env clojure
(def fibs
  (lazy-cat [(BigInteger/ZERO) (BigInteger/ONE)] (map + fibs (rest fibs))))

(println (count (take-while #(< % (.pow (BigInteger/TEN) 999)) fibs)))
