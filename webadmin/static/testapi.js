// const api_url = "http://localhost:8006/stats/users";
const api_url = "https://api.seaofkeys.com/stats/users";

// Define the session cookies as an object
// Create a Headers object and add the cookies to it

// const headers = new Headers();
// headers.append("Authorization", `${session_cookies}`);

// Define the URL for the fetch request
// const session_cookiess = "Jdfsd";

// Define the fetch request
fetch(api_url, {
  method: "GET",
  credentials: "include",
  // headers: {
  //   Authorization: `${session_cookies}`,
  //   sessin_id: `${session_cookies}`,
  // },
})
  .then((response) => {
    if (response.ok) {
      return response.json();
    } else {
      console.log("Not Okay");
      throw new Error("Network response was not ok");
    }
  })
  .then((data) => {
    // Handle the response data here
    console.log(data);
  })
  .catch((error) => {
    // Handle errors here
    console.error("There was a problem with the fetch operation:", error);
  });
