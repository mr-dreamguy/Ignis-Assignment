import parse from "html-react-parser";

function Description({ description }) {
  return (
    <div>
      <h4>Description</h4>
      {parse(description)}
    </div>
  );
}

export default Description;
