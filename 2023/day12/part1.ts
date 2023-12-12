import { getParsedData } from "../common/index.ts";

function* getAllCombinations(iterable: number[], r: number) {
  // copied from python
  // from itertools import combinations
  const pool = [...iterable];
  const n = pool.length;

  if (r > n) {
    return;
  }

  const indices = Array.from({ length: r }, (_, i) => i);

  yield indices.map((i) => pool[i]);

  while (true) {
    let i;
    for (i = r - 1; i >= 0; i--) {
      if (indices[i] !== i + n - r) {
        break;
      }
    }

    if (i === -1) {
      return;
    }

    indices[i]++;
    for (let j = i + 1; j < r; j++) {
      indices[j] = indices[j - 1] + 1;
    }

    yield indices.map((i) => pool[i]);
  }
}

const checkIfCombinationPossible = (
  combination: number[],
  conditions: string,
  lengths: number[]
) => {
  let result = "";
  let startIndex = 0;

  for (let _ = 0; _ < combination[0]; _++) {
    result += ".";
  }

  for (let i = 0; i < combination.length; i++) {
    const l = lengths[i];
    const c = combination[i];

    startIndex += c;

    for (let _ = startIndex; _ < startIndex + l; _++) {
      result += "#";
    }

    if (i < combination.length)
      for (let _ = 0; _ < combination[i + 1] - c; _++) {
        result += ".";
      }
  }
  for (let _ = result.length; _ < conditions.length; _++) {
    result += ".";
  }

  for (let index = 0; index < conditions.length; index++) {
    const ogElement = conditions[index];
    const proposedElement = result[index];

    const twoChars = ogElement + proposedElement;
    if (["#.", ".#"].includes(twoChars)) return false;
  }
  return true;
};

const getLinePossibilities = (line: string): number => {
  const split = line.split(" ");
  const springConditions = split[0];
  const springOrder = split[1].split(",").map((v) => parseInt(v));

  const combinations = [
    ...getAllCombinations(
      Array.from(
        {
          length:
            1 +
            springConditions.length -
            springOrder.reduce((acc, v) => acc + v),
        },
        (_, i) => i
      ),
      springOrder.length
    ),
  ];

  let total = 0;
  for (const comb of combinations) {
    total += +checkIfCombinationPossible(comb, springConditions, springOrder);
  }
  return total;
};

const main = async (): Promise<number> => {
  const data = await getParsedData(12);
  return data.map(getLinePossibilities).reduce((acc, v) => acc + v);
};

console.log(await main());
