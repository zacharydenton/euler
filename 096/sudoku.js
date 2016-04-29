const fs = require("fs")
const digits = "123456789"

function parseGames(gameFile) {
  return gameFile.toString().split(/Grid \d+\n/).slice(1).map((gameString) => {
    return gameString.split("\n").join("")
  })
}

function parseGame(gameString) {
  const game = []
  for (let x = 0; x < 9; x++) {
    game[x] = []
    for (let y = 0; y < 9; y++) {
      game[x][y] = digits
    }
  }
  gameString.split("").forEach((c, i) => {
    const x = i % 9
    const y = Math.floor(i / 9)
    if (c !== "0") {
      move(game, x, y, c)
    }
  })
  return game
}

function units(x, y) {
  const result = [[], [], []]
  for (let i = 0; i < 9; i++) {
    const col = [x, i]
    result[0].push(col)
    const row = [i, y]
    result[1].push(row)
  }
  for (let sx = Math.floor(x / 3) * 3, i = sx; i < sx + 3; i++) {
    for (let sy = Math.floor(y / 3) * 3, j = sy; j < sy + 3; j++) {
      const box = [i, j]
      result[2].push(box)
    }
  }
  return result.map((unit) => {
    return unit.filter(([ux, uy]) => !(ux === x && uy === y))
  })
}

const peerCache = {}
function peers(x, y) {
  if (peerCache[[x, y]]) {
    return peerCache[[x, y]]
  }
  const result = []
  const seen = {}
  units(x, y).forEach((unit) => {
    unit.forEach((pos) => {
      if (!seen[pos]) {
        seen[pos] = 1
        result.push(pos)
      }
    })
  })
  peerCache[[x, y]] = result
  return result
}

function move(game, x, y, c) {
  const otherValues = game[x][y].replace(c, "").split("")
  return otherValues.every((oc) => propagate(game, x, y, oc)) && game
}

function propagate(game, x, y, c) {
  if (game[x][y].indexOf(c) < 0) {
    return game
  }
  game[x][y] = game[x][y].replace(c, "")
  if (game[x][y].length === 0) {
    return false
  } else if (game[x][y].length === 1) {
    const ps = peers(x, y)
    for (let i = 0, l = ps.length; i < l; i++) {
      const [px, py] = ps[i]
      if (!propagate(game, px, py, game[x][y])) {
        return false
      }
    }
  }
  const us = units(x, y)
  for (let i = 0, l = us.length; i < l; i++) {
    const unit = us[i]
    const places = unit.filter(([ux, uy]) => game[ux][uy].indexOf(c) >= 0)
    if (places.length === 0) {
      return false
    } else if (places.length === 1) {
      const [px, py] = places[0]
      if (!move(game, px, py, c)) {
        return false
      }
    }
  }
  return game
}

function isSolved(game) {
  for (let x = 0; x < 9; x++) {
    for (let y = 0; y < 9; y++) {
      if (game[x][y].length !== 1) {
        return false
      }
    }
  }
  return true
}

function copyGame(game) {
  const copy = []
  for (let x = 0; x < 9; x++) {
    copy[x] = []
    for (let y = 0; y < 9; y++) {
      copy[x][y] = game[x][y]
    }
  }
  return copy
}

function solve(game) {
  if (!game) {
    return false
  } else if (isSolved(game)) {
    return game
  }
  let nx, ny
  let min = Infinity
  for (let x = 0; x < 9; x++) {
    for (let y = 0; y < 9; y++) {
      if (game[x][y].length > 1 && game[x][y].length < min) {
        min = game[x][y].length
        nx = x
        ny = y
      }
    }
  }
  const choices = game[nx][ny].split("")
  for (let i = 0, l = choices.length; i < l; i++) {
    const copy = copyGame(game)
    const solution = solve(move(copy, nx, ny, choices[i]))
    if (solution) {
      return solution
    }
  }
  return false
}

const games = parseGames(fs.readFileSync(__dirname + "/sudoku.txt"))
console.log(games.reduce((acc, gameString) => {
  const game = parseGame(gameString)
  const solution = solve(game)
  const topLeft = parseInt(solution[0][0] + solution[1][0] + solution[2][0])
  return acc + topLeft
}, 0))
