import React, { useState } from 'react';

function Search() {
  // State to store the search query
  const [searchQuery, setSearchQuery] = useState('');

  // Function to handle the change in input
  const handleInputChange = (event) => {
    setSearchQuery(event.target.value);
  };

  // Optional: Function to handle form submission
  const handleSearchSubmit = (event) => {
    event.preventDefault();
    // Perform the search operation with searchQuery
    console.log('Searching for:', searchQuery);
    // You can replace the console.log with actual search logic
  };

  return (
    <div>
      {/* Optional: Wrap the input in a form for submission */}
      <form onSubmit={handleSearchSubmit}>
        <input
          type="text"
          placeholder="Search..."
          value={searchQuery}
          onChange={handleInputChange}
        />
        {/* Optional: Add a submit button */}
        <button type="submit">Search</button>
      </form>
    </div>
  );
}

export default Search;