// import * as React from 'react';
// import Box from '@mui/material/Box';
// import Button from '@mui/material/Button';
// import Card from '@mui/material/Card';
// import Chip from '@mui/material/Chip';
// import Container from '@mui/material/Container';
// import Grid from '@mui/material/Grid';
// import Link from '@mui/material/Link';
// import Stack from '@mui/material/Stack';
// import Typography from '@mui/material/Typography';
// import ChevronRightRoundedIcon from '@mui/icons-material/ChevronRightRounded';
// import DevicesRoundedIcon from '@mui/icons-material/DevicesRounded';
// import EdgesensorHighRoundedIcon from '@mui/icons-material/EdgesensorHighRounded';
// import ViewQuiltRoundedIcon from '@mui/icons-material/ViewQuiltRounded';

// const items = [
//   {
//     icon: <ViewQuiltRoundedIcon />,
//     title: 'Current AQI',
//     description:
//       '',
//     imageLight: 'url("/static/images/templates/templates-images/dash-light.png")',
//     imageDark: 'url("/static/images/templates/templates-images/dash-dark.png")',
//   },
// ];

// export default function Features() {
//   const [selectedItemIndex, setSelectedItemIndex] = React.useState(0);

//   const handleItemClick = (index) => {
//     setSelectedItemIndex(index);
//   };

//   const selectedFeature = items[selectedItemIndex];

//   return (
//     <Container id="features" sx={{ py: { xs: 8, sm: 16 } }}>
//       <Grid container spacing={6}>
//         <Grid item xs={12} md={6}>
//           {/* <Grid container item gap={1} sx={{ display: { xs: 'auto', sm: 'none' } }}>
//             {items.map(({ title }, index) => (
//               <Chip
//                 key={index}
//                 label={title}
//                 onClick={() => handleItemClick(index)}
//                 sx={{
//                   borderColor: (theme) => {
//                     if (theme.palette.mode === 'light') {
//                       return selectedItemIndex === index ? 'primary.light' : '';
//                     }
//                     return selectedItemIndex === index ? 'primary.light' : '';
//                   },
//                   background: (theme) => {
//                     if (theme.palette.mode === 'light') {
//                       return selectedItemIndex === index ? 'none' : '';
//                     }
//                     return selectedItemIndex === index ? 'none' : '';
//                   },
//                   backgroundColor: selectedItemIndex === index ? 'primary.main' : '',
//                   '& .MuiChip-label': {
//                     color: selectedItemIndex === index ? '#fff' : '',
//                   },
//                 }}
//               />
//             ))}
//           </Grid> */}
//           <Box
//             component={Card}
//             variant="outlined"
//             sx={{
//               display: { xs: 'auto', sm: 'none' },
//               mt: 4,
//             }}
//           >
//             <Box
//               sx={{
//                 backgroundImage: (theme) =>
//                   theme.palette.mode === 'light'
//                     ? items[selectedItemIndex].imageLight
//                     : items[selectedItemIndex].imageDark,
//                 backgroundSize: 'cover',
//                 backgroundPosition: 'center',
//                 minHeight: 280,
//               }}
//             />
//             <Box sx={{ px: 2, pb: 2 }}>
//               <Typography color="text.primary" variant="body2" fontWeight="bold">
//                 {selectedFeature.title}
//               </Typography>
//               <Typography color="text.secondary" variant="body2" sx={{ my: 0.5 }}>
//                 {selectedFeature.description}
//               </Typography>
//               {/* <Link
//                 color="primary"
//                 variant="body2"
//                 fontWeight="bold"
//                 sx={{
//                   display: 'inline-flex',
//                   alignItems: 'center',
//                   '& > svg': { transition: '0.2s' },
//                   '&:hover > svg': { transform: 'translateX(2px)' },
//                 }}
//               >
//                 <span>Learn more</span>
//                 <ChevronRightRoundedIcon
//                   fontSize="small"
//                   sx={{ mt: '1px', ml: '2px' }}
//                 />
//               </Link> */}
//             </Box>
//           </Box>
//           <Stack
//             direction="column"
//             justifyContent="center"
//             alignItems="flex-center"
//             spacing={2}
//             // useFlexGap
//             sx={{ width: '100%', display: { xs: 'none', sm: 'flex' } }}
//           >
//             {items.map(({ icon, title, description }, index) => (
//               <Card
//                 key={index}
//                 variant="outlined"
//                 component={Button}
//                 onClick={() => handleItemClick(index)}
//                 sx={{
//                   p: 3,
//                   height: 'fit-content',
//                   width: '100%',
//                   background: 'none',
//                   backgroundColor:
//                     selectedItemIndex === index ? 'action.selected' : undefined,
//                   borderColor: (theme) => {
//                     if (theme.palette.mode === 'light') {
//                       return selectedItemIndex === index
//                         ? 'primary.light'
//                         : 'grey.200';
//                     }
//                     return selectedItemIndex === index ? 'primary.dark' : 'grey.800';
//                   },
//                 }}
//               >
//                 <Box
//                   sx={{
//                     width: '100%',
//                     display: 'flex',
//                     textAlign: 'left',
//                     flexDirection: { xs: 'column', md: 'row' },
//                     alignItems: { md: 'center' },
//                     gap: 2.5,
//                   }}
//                 >
//                   <Box
//                     sx={{
//                       color: (theme) => {
//                         if (theme.palette.mode === 'light') {
//                           return selectedItemIndex === index
//                             ? 'primary.main'
//                             : 'grey.300';
//                         }
//                         return selectedItemIndex === index
//                           ? 'primary.main'
//                           : 'grey.700';
//                       },
//                     }}
//                   >
//                     {icon}
//                   </Box>
//                   <Box sx={{ textTransform: 'none' }}>
//                     <Typography
//                       color="text.primary"
//                       variant="body2"
//                       fontWeight="bold"
//                     >
//                       {title}
//                     </Typography>
//                     <Typography
//                       color="text.secondary"
//                       variant="body2"
//                       sx={{ my: 0.5 }}
//                     >
//                       {description}
//                     </Typography>
//                   </Box>
//                 </Box>
//               </Card>
//             ))}
//           </Stack>
//         </Grid>
//         {/* <Grid
//           item
//           xs={12}
//           md={6}
//           sx={{ display: { xs: 'none', sm: 'flex' }, width: '100%' }}
//         > */}
//           {/* <Card
//             variant="outlined"
//             sx={{
//               height: '100%',
//               width: '100%',
//               display: { xs: 'none', sm: 'flex' },
//               pointerEvents: 'none',
//             }}
//           >
//             <Box
//               sx={{
//                 m: 'auto',
//                 width: 420,
//                 height: 500,
//                 backgroundSize: 'contain',
//                 backgroundImage: (theme) =>
//                   theme.palette.mode === 'light'
//                     ? items[selectedItemIndex].imageLight
//                     : items[selectedItemIndex].imageDark,
//               }}
//             />
//           </Card> */}
//         {/* </Grid> */}
//       </Grid>
//     </Container>
//   );
// }






import * as React from 'react';
import { useState, useEffect } from 'react';
import Box from '@mui/material/Box';
import Button from '@mui/material/Button';
import Card from '@mui/material/Card';
import Chip from '@mui/material/Chip';
import Container from '@mui/material/Container';
import Grid from '@mui/material/Grid';
import Link from '@mui/material/Link';
import Stack from '@mui/material/Stack';
import Typography from '@mui/material/Typography';
import ChevronRightRoundedIcon from '@mui/icons-material/ChevronRightRounded';
import DevicesRoundedIcon from '@mui/icons-material/DevicesRounded';
import EdgesensorHighRoundedIcon from '@mui/icons-material/EdgesensorHighRounded';
import ViewQuiltRoundedIcon from '@mui/icons-material/ViewQuiltRounded';

const Features = () => {
  const [aqiData, setAqiData] = useState({ currentAqi: is });

  useEffect(() => {
    // Replace '/search' with your actual endpoint
    fetch('/search', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      // Replace this body with the actual data required by your backend
      body: JSON.stringify({ city: 'YourCityName' }),
    })
    .then(response => response.json())
    .then(data => {
      // Assuming the response has a property named 'aqi'
      setAqiData({ currentAqi: data.aqi });
    })
    .catch(error => console.error('Error:', error));
  }, []);

  const items = [
    {
      icon: <ViewQuiltRoundedIcon />,
      title: 'Current AQI',
      description: aqiData.currentAqi,
      imageLight: 'url("/static/images/templates/templates-images/dash-light.png")',
    },
    // Add other items here
  ];

  return (
    <Container>
      {/* Your existing JSX structure */}
      <Grid container spacing={2}>
        {items.map((item, index) => (
          <Grid item key={index} xs={12} sm={6} md={4}>
            <Card>
              <Box sx={{ p: 2, display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
                {item.icon}
                <Typography variant="h6">{item.title}</Typography>
                <Typography>{item.description}</Typography>
              </Box>
            </Card>
          </Grid>
        ))}
      </Grid>
    </Container>
  );
};

export default Features;