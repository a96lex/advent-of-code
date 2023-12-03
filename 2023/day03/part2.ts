import { getParsedData } from "../common/index.ts";

type Point = {
  x: number;
  y: number;
  value: number;
};

type NumberPoint = Point & {
  l: number;
};

const parseLine = (
  symbols: Point[],
  points: NumberPoint[],
  line: string,
  lineY: number
): void => {
  // get numbers
  const re = /\d+/g;
  let match: RegExpExecArray | null;
  while ((match = re.exec(line)) != null) {
    points.push({
      value: parseInt(match[0]),
      x: match.index,
      y: lineY,
      l: match[0].length,
    });
  }
  // get symbols
  const re2 = /\*/g;
  while ((match = re2.exec(line)) != null) {
    symbols.push({
      x: match.index,
      y: lineY,
      value: 1,
    });
  }
};

const getNeighbours = (point: NumberPoint): Point[] => {
  const neighbours: Point[] = [];
  // leftmost
  neighbours.push({
    x: point.x - 1,
    y: point.y,
    value: point.value,
  });
  //rightmost
  neighbours.push({
    x: point.x + point.l,
    y: point.y,
    value: point.value,
  });
  // top and bottom
  for (let i = -1; i < point.l + 1; i += 1) {
    neighbours.push({
      x: point.x + i,
      y: point.y + 1,
      value: point.value,
    });
    neighbours.push({
      x: point.x + i,
      y: point.y - 1,
      value: point.value,
    });
  }

  const cleanNeigbours = neighbours.filter(
    (n) => n.x >= 0 && n.y >= 0 && n.x < 140 && n.y < 140
  );
  return cleanNeigbours;
};

const main = async (): Promise<number> => {
  const data = await getParsedData(3);
  const points: NumberPoint[] = [];
  const symbols: Point[] = [];

  const gearRatios: { [key: string]: number[] } = {};

  data.map((line, index) => parseLine(symbols, points, line, index));

  points.filter((point) =>
    getNeighbours(point).map((n) => {
      symbols.map((s) => {
        if (s.x === n.x && s.y === n.y) {
          const pointStr = `${s.x},${s.y}`;
          if (gearRatios[pointStr]) {
            gearRatios[pointStr].push(n.value);
          } else {
            gearRatios[pointStr] = [n.value];
          }
        }
      });
    })
  );

  const res = Object.keys(gearRatios)
    .map((key) => {
      if (gearRatios[key].length === 2) {
        return gearRatios[key][0] * gearRatios[key][1];
      }
      return 0;
    })
    .reduce((a, b) => a + b, 0);

  return res;
};

console.log(await main());
