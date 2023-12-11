import { getParsedData } from "../common/index.ts";

type Galaxy = {
  x: number;
  y: number;
};

const parseData = (
  data: string[]
): { galaxyPositions: Galaxy[]; emptyX: number[]; emptyY: number[] } => {
  const galaxyPositions: Galaxy[] = [];

  for (let y = 0; y < data.length; y++) {
    const line = data[y];
    for (let x = 0; x < line.length; x++) {
      if (line[x] === "#") galaxyPositions.push({ x, y });
    }
  }

  const emptyX: number[] = Array.from(
    { length: data[0].length },
    (_, index) => index
  ).filter((x) => !galaxyPositions.some((g) => g.x === x));
  const emptyY: number[] = Array.from(
    { length: data.length },
    (_, index) => index
  ).filter((y) => !galaxyPositions.some((g) => g.y === y));
  return { galaxyPositions, emptyX, emptyY };
};

const isInRange = (value: number, start: number, end: number): boolean => {
  let small = 0,
    big = 0;
  if (start > end) (small = end), (big = start);
  if (start <= end) (small = start), (big = end);
  return value >= small && value < big;
};

const main = async (): Promise<number> => {
  const data = await getParsedData(11);
  const { galaxyPositions, emptyX, emptyY } = parseData(data);

  let accDistance = 0;
  for (let g1 = 0; g1 < galaxyPositions.length; g1++) {
    const galaxy1 = galaxyPositions[g1];
    for (let g2 = g1 + 1; g2 < galaxyPositions.length; g2++) {
      const galaxy2 = galaxyPositions[g2];
      let distance =
        Math.abs(galaxy1.x - galaxy2.x) + Math.abs(galaxy1.y - galaxy2.y);

      for (const x of emptyX) {
        if (isInRange(x, galaxy1.x, galaxy2.x)) distance += 999999;
      }

      for (const y of emptyY) {
        if (isInRange(y, galaxy1.y, galaxy2.y)) distance += 999999;
      }

      accDistance += distance;
    }
  }
  return accDistance;
};

console.log(await main());
