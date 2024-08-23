import { useState, useEffect } from "react";
import api from "../api";

function Home() {
  let [categories, setCategories] = useState([]);

  useEffect(() => {
    getCategories();
  }, []);

  const getCategories = () => {
    api
      .get("/category/")
      .then((res) => res.data)
      .then((data) => setCategories(data))
      .catch((err) => {
        alert(err);
        console.log(err);
      });
  };

  return (
    <div
      className="ms-center"
      style={{
        width: "500px",
        textAlign: "center",
        margin: "auto",
      }}
    >
      <h1>All Categories</h1>
      <div className="list-group">
        {categories.map((cat) => (
          <div key={cat.id}>
            <a
              className="list-group-item list-group-item-action list-group-item-primary"
              href={`/category/${cat.id}`}
            >
              {cat.name}
            </a>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Home;
