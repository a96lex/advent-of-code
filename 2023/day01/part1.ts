import { getParsedData } from "../common/index.ts";

const sumFirstAndLastDigits = (calibration: string): number => {
  // find first occurance of a digit in the string
  const digits = calibration.match(/\d/g);
  if (!digits) return 0;
  return parseInt(digits[0] + digits[digits.length - 1]);
};

const part1 = async (): Promise<number> => {
  const data = await getParsedData(1);
  const nums = data.map((x) => sumFirstAndLastDigits(x));
  return nums.reduce((a, b) => a + b);
};

console.log(await part1());
