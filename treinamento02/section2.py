from flet import *
from flet import colors, icons

sectio2= ResponsiveRow([
    Container(
        bgcolor="#FFFFF",
        border_radius= border_radius.only(top_left=30, top_right=30),
        padding=0,
        margin=margin.symmetric(vertical=-30),
        content=Column(col={"sm":12, "md":12, "lg":12},
            controls=[
                # for input search lunch
            Container(
                bgcolor="#FCFCFC",
                border_radius=30,

                content=Row([
                    TextField(
                    border="none",
                    prefix_icon=icons.SEARCH,
                    label="Search Lunch ?"
                    ),
                IconButton(icon= icons.ACCOUNT_CIRCLE,
                           icon_color="green",
                           icon_size=30
                           ),

                ])
            ),
            # for blue card
            Card(
                elevation=30,
                content=Container(
                    border_radius=30,
                    bgcolor="#01ADD5",
                    content=Row([
                        Container(
                            margin=10,
                            height=70,
                            padding=10,
                            width=120,
                            border_radius=10,
                            bgcolor="white",
                            content=Column([
                                Text("gopay", weight="bold", size=15
                                ),
                                Text("RP.7.029", weight="bold", size=17
                                ),
                                Text("Tap to Top Up", size=11
                                ),
                            ], alignment="center", spacing=0)
                        ),
                        # for child icon
                        Column([
                            Icon(name="bolt",color="white",size=30
                                 ),
                            Text("Pay", color="white", size=15,
                                 weight="bold")
                        ]),
                         Column([
                            Icon(name="add_box",color="white",size=30
                                 ),
                            Text("Top Up", color="white", size=15,
                                 weight="bold")
                        ]),
                         Column([
                            Icon(name="drag_indicator",color="white",size=30
                                 ),
                            Text("More", color="white", size=15,
                                 weight="bold")
                        ]),
                    ], alignment="spaceEvenly")
                )
            )
        ])
    )
])