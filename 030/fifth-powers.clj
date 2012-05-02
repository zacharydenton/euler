#!/usr/bin/env clojure
(defn ** [x n]
  (. (. java.math.BigInteger (valueOf x)) (pow n)))

(defn digits [number]
  (map #(- (int %) 48) (str number))) 

(defn can-be-written-as-sum-of-fifths? [number]
  (and (not (= number 1)) (= (apply + (map #(** % 5) (digits number))) number)))

(println (reduce + (filter can-be-written-as-sum-of-fifths? (range 500000))))
