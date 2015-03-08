require(shiny)
load('job.result.rda')
toolnames <-c("Python","R","SQL","EXCEL","C","MATLAB","C++","Hive","Spark","Unix","Perl","Total")

shinyUI(pageWithSidebar(
    headerPanel('Data Science Skills Map'),
    sidebarPanel(
        helpText("Choose the tool"),
        selectInput('Tools','Tool', toolnames, 
                    selected=toolnames[1]),## name:"Tools"
        br(),p(" The maps depicting regional data science skills needs in the US data scientist job market",
      a("Our Source Code", 
        href = " http://www.github.com/yiginger")),
      br(),
     p("Supported by ",
       a("CornelTech Data Hackathon" ,
         href = "http://datahackathon2015.splashthat.com")
     )),
    mainPanel(
      h2("Data Science Skills Needs Map",align = "center"),
        plotOutput('plotMap',height="600px")
    )
))

