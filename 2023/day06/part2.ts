import { getParsedData } from "../common/index.ts";

const parseLine = (line: string): number[] => {
  const regex = /\d+/g;
  return line
    .replaceAll(" ", "")
    .match(regex)!
    .map((n) => parseInt(n));
};

const isInteger = (n: number): boolean => {
  return n % 1 === 0;
};

const computeWinningHold = (time: number, distance: number): number => {
  let minHold = (time - Math.sqrt(time ** 2 - 4 * distance)) / 2;
  if (isInteger(minHold)) {
    minHold += 1;
  } else {
    minHold = Math.ceil(minHold);
  }

  let maxHold = (time + Math.sqrt(time ** 2 - 4 * distance)) / 2;
  if (isInteger(maxHold)) {
    maxHold -= 1;
  } else {
    maxHold = Math.floor(maxHold);
  }

  return maxHold - minHold + 1;
};

const main = async (): Promise<number> => {
  const data = await getParsedData(6);
  const times = parseLine(data[0]);
  const distances = parseLine(data[1]);

  const winningHolds = times.map((value, index) =>
    computeWinningHold(value, distances[index])
  );

  const res = winningHolds.reduce((acc, value) => acc * value, 1);

  return res;
};

console.log(await main());
