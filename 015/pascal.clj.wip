#!/usr/bin/env clojure
; compute pascal's triangle
(defn ** [x n]
  (. (. java.math.BigInteger (valueOf x)) (pow n)))

(defn pascal [n k]
  (cond 
    (= k n) 1
    (or (< n 0) (< k 0)) 0
    :else 
    (+
      (pascal (- n 1) (- k 1))
      (pascal (- n 1) k))))

(defn pascal-row [n]
  (map #(pascal n %) (range (+ n 1))))

(defn pascal-triangle [num-rows]
  (map #(pascal-row %) (range num-rows)))

(dorun (map println (pascal-triangle 10)))
(println (pascal 5 3))
