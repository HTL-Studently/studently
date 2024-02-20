interface Params {
    slug: string;
}

interface Props {
    title: string;
}

export function load({ params }: { params: Params }): { props: Props } {
    return {
        props: {
            title: params.slug
        }
    };
}
