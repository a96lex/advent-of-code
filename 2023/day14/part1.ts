import { getParsedData } from "../common/index.ts";

const parseGrid = (input: string[]) => {
  return input.map((v) => v.split(""));
};

const transpose = (matrix: string[][]) => {
  return matrix[0].map((_, i) => matrix.map((row) => row[i]));
};

const reorderLine = (line: string[]) => {
  console.log(line.join());
  for (let i = 1; i < line.length; i++) {
    const element = line[i];
    if (element == "O") {
      let targetIndex = i - 1;
      while (targetIndex >= 0 && line[targetIndex] === ".") {
        targetIndex--;
      }
      line[i] = ".";
      line[targetIndex + 1] = "O";
    }
  }
  return line;
};

const main = async (): Promise<number> => {
  const data = await getParsedData(14);
  const grid = transpose(parseGrid(data));
  console.log(grid.map((v) => v.join()));
  const res = grid
    .map(reorderLine)
    .map((line) =>
      line
        .map((el, idx) => {
          if (el === "O") {
            return grid[0].length - idx;
          }
          return 0;
        })
        .reduce((acc, val) => acc + val)
    )
    .reduce((acc, val) => acc + val);

  console.log(res);

  return 0;
};

console.log(await main());
