import api from "../api";
import { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import ImageCards from "./ImageCards";

function Category() {
  let [category, setCategory] = useState({});
  let { id } = useParams();

  useEffect(() => {
    getCategory();
  }, [id]);

  let getCategory = () => {
    api
      .get(`/category/${id}`)
      .then((res) => res.data)
      .then((data) => setCategory(data[0]))
      .catch((err) => {
        alert(err);
        console.log(err);
      });
  };

  return (
    <div>
      {category.name ? (
        <div>
          <h1>{category.name}</h1>
          <ImageCards id={id} />
        </div>
      ) : null}
    </div>
  );
}

export default Category;
