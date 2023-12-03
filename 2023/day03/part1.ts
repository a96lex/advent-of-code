import { getParsedData } from "../common/index.ts";

type Point = {
  x: number;
  y: number;
};

type NumberPoint = Point & {
  value: number;
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
  const re2 = /[^0-9.]/g;
  while ((match = re2.exec(line)) != null) {
    symbols.push({
      x: match.index,
      y: lineY,
    });
  }
};

const getNeighbours = (point: NumberPoint): Point[] => {
  const neighbours: Point[] = [];
  // leftmost
  neighbours.push({
    x: point.x - 1,
    y: point.y,
  });
  //rightmost
  neighbours.push({
    x: point.x + point.l,
    y: point.y,
  });
  // top and bottom
  for (let i = -1; i < point.l + 1; i += 1) {
    neighbours.push({
      x: point.x + i,
      y: point.y + 1,
    });
    neighbours.push({
      x: point.x + i,
      y: point.y - 1,
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
  data.map((line, index) => parseLine(symbols, points, line, index));
  const res = points
    .filter((point) =>
      getNeighbours(point).some((n) =>
        symbols.some((s) => s.x === n.x && s.y === n.y)
      )
    )
    .reduce((acc, curr) => acc + curr.value, 0);

  return res;
};

console.log(await main());
