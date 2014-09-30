#!/usr/bin/env clojure
(defn raise [x n]
  (. (. java.math.BigInteger (valueOf x)) (pow n)))

(defn raise-to-itself [number]
  (raise number number))

(defn digits [n]
  (map #(- (int %) 48) (str n)))

(def result (reduce + (map raise-to-itself (range 1 1001))))
(println (apply str (reverse (take 10 (reverse (digits result))))))
