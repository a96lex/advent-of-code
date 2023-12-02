import { getParsedData } from "../common/index.ts";

const parseLine = (
  line: string
): { id: number; maxVals: { red: number; green: number; blue: number } } => {
  const id = parseInt(line.split(":")[0].split(" ")[1]);

  const maxVals = {
    red: 0,
    green: 0,
    blue: 0,
  };

  line
    .split(":")[1]
    .split(";")
    .map((round) => {
      const balls = round.split(",");
      for (const ball of balls) {
        const [_, value, color] = ball.split(" ") as [
          string,
          string,
          keyof typeof maxVals
        ];

        if (parseInt(value) > maxVals[color]) {
          maxVals[color] = parseInt(value);
        }
      }
    });

  return { id, maxVals };
};

const main = async (): Promise<number> => {
  const data = await getParsedData(2);
  const parsedData = data.map(parseLine);

  const sumOfPowers = parsedData.reduce(
    (
      acc: number,
      line: {
        id: number;
        maxVals: { red: number; green: number; blue: number };
      }
    ) => {
      return acc + line.maxVals.red * line.maxVals.green * line.maxVals.blue;
    },
    0
  );

  return sumOfPowers;
};

console.log(await main());
