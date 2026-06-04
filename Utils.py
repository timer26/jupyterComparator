from IPython.display import display, HTML

def show(df, title, start=0, rows=100, persistence_data=None):
    total_rows = len(df)
    end = min(start + rows, total_rows)
    slice_df = df.iloc[start:end]
    display(HTML(f"<h3>{title} — rows {start}–{end} of {total_rows}</h3>"))

    if persistence_data is not None and len(persistence_data) > 0:
        display(HTML(f"""
            <div style="width: 100%; overflow-x: visible;">
                {persistence_data.to_html()}
            </div>
        """))

    display(HTML(f"""
        <div style="overflow-x: scroll;
        overflow-y: auto;
        max-height: 400px;
        width: 100%;
        display: block;">
            {slice_df.to_html()}
        </div>
    """))