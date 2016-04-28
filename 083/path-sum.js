const fs = require("fs")

function parseMatrix(matrix) {
  return matrix.toString().trim().split("\n").map((line) => {
    return line.split(",").map((c) => parseInt(c))
  })
}

function bfs(graph, root, target) {
  function neighbors([x, y]) {
    const candidates = [
      [x - 1, y],
      [x + 1, y],
      [x, y - 1],
      [x, y + 1]
    ]
    return candidates.filter(([x, y]) => {
      return x >= 0 && x < graph[0].length && y >= 0 && y < graph.length
    })
  }

  function evaluate(path) {
    return path.reduce((acc, [x, y]) => acc + graph[y][x], 0)
  }

  const start = [root]
  const frontier = [[evaluate(start), start]]
  const explored = new Set()
  while (frontier.length > 0) {
    let path = null
    let min = Infinity
    let index = -1
    frontier.forEach(([score, candidate], i) => {
      if (score < min) {
        min = score
        path = candidate
        index = i
      }
    })
    frontier.splice(index, 1)
    const node = path[path.length - 1]
    explored.add(node.toString())
    if (node.toString() === target.toString()) {
      return min
    }
    neighbors(node).forEach((neighbor) => {
      if (!explored.has(neighbor.toString())) {
        const newPath = path.slice()
        newPath.push(neighbor)
        frontier.push([evaluate(newPath), newPath])
      }
    })
  }
}

const graph = parseMatrix(fs.readFileSync(__dirname + "/matrix.txt"))
console.log(bfs(graph, [0, 0], [graph[0].length - 1, graph.length - 1]))
