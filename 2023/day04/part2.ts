import { getParsedData } from "../common/index.ts";

const getLineMatches = (line: string): number => {
  const numbers = line.replaceAll("  ", " ").split(":")[1].split("|");
  const winningNumbers = numbers[0]
    .trim()
    .split(" ")
    .map((n) => parseInt(n));
  const ownedNumbers = numbers[1]
    .trim()
    .split(" ")
    .map((n) => parseInt(n));
  const guessedNumbers = ownedNumbers.filter((n) => winningNumbers.includes(n));

  if (guessedNumbers.length === 0) {
    return 0;
  }

  return guessedNumbers.length;
};

const main = async (): Promise<number> => {
  const data = await getParsedData(4);
  const weights = data.map(() => 1);
  const values = data.map((line) => getLineMatches(line));

  values.forEach((v, i) => {
    for (let j = i + 1; j <= i + v; j++) {
      if (j <= values.length) {
        weights[j] += weights[i];
      }
    }
  });

  const result = weights.reduce((a, b) => a + b, 0);
  return result;
};

console.log(await main());
