import "https://deno.land/std@0.170.0/dotenv/load.ts";

const YEAR = 2023;

const dayToString = (day: number): string => {
  return day.toString().padStart(2, "0");
};

const getInputData = async (day: number): Promise<string> => {
  const filename = `./inputs/${dayToString(day)}.txt`;

  try {
    const stats = await Deno.lstat(filename);
    if (stats.isFile) {
      const text = await Deno.readTextFile(filename);
      return text;
    }
  } catch {
    // file doesn't exist
  }

  const data = await fetch(
    `https://adventofcode.com/${YEAR}/day/${day}/input`,
    {
      headers: {
        cookie: Deno.env.get("aoc_cookie") as string,
      },
    }
  );

  const content = await data.text();
  await Deno.writeTextFile(filename, content);

  return content;
};

const getParsedData = async (day: number) => {
  const data = await getInputData(day);
  const lines = data.split("\n");
  if (!lines[lines.length - 1]) lines.pop();
  return lines;
};

export { getInputData, getParsedData };
