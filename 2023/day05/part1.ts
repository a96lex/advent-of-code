import { getParsedData } from "../common/index.ts";

const parseMapData = (data: string[], maps: number[][][]) => {
  let currentMap: number[][] = [];
  for (let i = 2; i < data.length; i++) {
    if (data[i].includes(":")) {
      continue;
    }
    if (data[i] === "") {
      if (currentMap) {
        maps.push(currentMap);
      }
      currentMap = [];
    } else {
      currentMap.push(data[i].split(" ").map((n) => parseInt(n)));
    }
  }
  if (currentMap) {
    maps.push(currentMap);
  }
};

const isInRange = (value: number, start: number, length: number): boolean => {
  return value >= start && value < start + length;
};

const main = async (): Promise<number> => {
  const data = await getParsedData(5);

  const maps: number[][][] = [];

  const seeds = data[0]
    .replace("seeds: ", "")
    .split(" ")
    .map((n) => parseInt(n));

  parseMapData(data, maps);

  let minDistance = Infinity;

  for (const seed of seeds) {
    let currentValue: number = seed;
    for (const map of maps) {
      for (const line of map) {
        if (isInRange(currentValue, line[1], line[2])) {
          currentValue = line[0] + currentValue - line[1];
          break;
        }
      }
    }
    if (currentValue < minDistance) {
      minDistance = currentValue;
    }
  }

  return minDistance;
};

console.log(await main());
