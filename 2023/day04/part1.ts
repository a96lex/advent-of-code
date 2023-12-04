import { getParsedData } from "../common/index.ts";

const getLinePoints = (line: string): number => {
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

  return 2 ** (guessedNumbers.length - 1);
};

const main = async (): Promise<number> => {
  const data = await getParsedData(4);
  const result = data.reduce((acc, line) => acc + getLinePoints(line), 0);
  return result;
};

console.log(await main());
