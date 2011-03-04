#!/usr/bin/env clojure
(defn square [x]
  (* x x))

(defn sum-squares [limit]
  (apply + (map square (range 1 (+ limit 1)))))

(defn square-sum [limit]
  (square (apply + (range 1 (+ limit 1)))))

(println (- (square-sum 100) (sum-squares 100)))
