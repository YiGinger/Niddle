require(shiny)
load("job.result.rda")
require(maps)
require(mapproj)
plotmap = function(Tools="R") 
{
    ## Tools: which tools to choose from 2:R,Python 
    ## option: which option to choose,depend on each questions
    ## color: choose a color for plotting
    ## advice color: darkgreen,purple,gray10,blue
  
    data1 = df[,tolower(Tools)]
    plotdata2 = data.frame(proportion=data1,
                          region=tolower(df$State))
    map = map_data("state")
    
    usmap = ggplot(data=plotdata2) + 
        geom_map(map =map,
                 aes(map_id = region,fill= proportion),
                 color="grey40") +
        expand_limits(x = map$long, y = map$lat) +
        scale_fill_continuous(high="red",low='white') +
      coord_map("polyconic",xlim=c(-120,-71))+
      ##---------Modify-----------------------
    theme(axis.text=element_blank(),
          axis.ticks=element_blank(),
          axis.title=element_blank(),
          panel.grid.major=element_blank(),
          panel.background=element_blank(),
          legend.position=c(0.95,0.28))
    
    print(usmap)
}

shinyServer(function(input, output, session) 
{
    require(ggplot2)
    load('job.result.rda')  
    
    selectedMap = reactive({
        tool.ind =tolower(input$Tools)
    })
    
    output$plotMap = renderPlot({
        inds = selectedMap()
        plotmap(inds)
    })
    
})
