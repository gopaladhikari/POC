type Props = {
  query: string;
};

export function SearchUsers({ query }: Props) {
  return <div> Search Query : {query}</div>;
}
